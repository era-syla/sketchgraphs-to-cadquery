import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00078, -0.00392).threePointArc((0.00283, -0.00283), (0.00392, -0.00078)).lineTo(0.00343, -0.00068).threePointArc((0.00323, -0.00134), (0.00291, -0.00194)).lineTo(0.00312, -0.00208).threePointArc((0.00265, -0.00265), (0.00208, -0.00312)).lineTo(0.00194, -0.00291).threePointArc((0.00134, -0.00323), (0.00068, -0.00343)).lineTo(0.00078, -0.00392).close()
solid=wp_sketch0.add(loop0).extrude(0.0010595755701226124)
