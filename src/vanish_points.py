import numpy as np

from .util import cm2inch, paper_dimensions, save_pdf, prepare_plot, draw_vanish_points, draw_horizon_line

def one_vanish_point(vp_cm, page_dimensions_cm, output_file, num_lines=30, horizon_line='h'):
    if horizon_line == 'h':
        horizon_line = 0
    elif horizon_line == 'v':
        horizon_line = 90
    elif type(horizon_line) not in (int, float):
        raise Exception(
            f'Invalid horizon line ({type(horizon_line)} -> {horizon_line})')
    
    ax, page_dimensions_inch = prepare_plot(paper_dimensions(page_dimensions_cm))
    
    draw_vanish_points([cm2inch(vp_cm)], page_dimensions_inch, num_lines, ax)
    draw_horizon_line(cm2inch(vp_cm), horizon_line, page_dimensions_inch, ax)
    
    save_pdf(output_file)
    
def two_vanish_point(vpA_cm, vpB_cm, page_dimensions_cm, output_file, num_lines=30):
    ax, page_dimensions_inch = prepare_plot(paper_dimensions(page_dimensions_cm))
    
    draw_vanish_points([cm2inch(vpA_cm), cm2inch(vpB_cm)], page_dimensions_inch, num_lines, ax)
    
    vec_x = vpA_cm[0] - vpB_cm[0]
    vec_y = vpA_cm[1] - vpB_cm[1]
    hip = np.linalg.norm((vec_x, vec_y))
    
    horizon_line = np.rad2deg(np.arccos(vec_x / hip))
    
    draw_horizon_line(cm2inch(vpA_cm), horizon_line, page_dimensions_inch, ax)
    
    save_pdf(output_file)
    
def three_vanish_point(vpA_cm, vpB_cm, vpC_cm, page_dimensions_cm, output_file, num_lines=30):
    ax, page_dimensions_inch = prepare_plot(paper_dimensions(page_dimensions_cm))
    
    draw_vanish_points([cm2inch(vpA_cm), cm2inch(vpB_cm), cm2inch(vpC_cm)], page_dimensions_inch, num_lines, ax)
    
    vec_x = vpA_cm[0] - vpB_cm[0]
    vec_y = vpA_cm[1] - vpB_cm[1]
    hip = np.linalg.norm((vec_x, vec_y))
    
    horizon_line = np.rad2deg(np.arccos(vec_x / hip))
    
    draw_horizon_line(cm2inch(vpA_cm), horizon_line, page_dimensions_inch, ax)
    
    save_pdf(output_file)