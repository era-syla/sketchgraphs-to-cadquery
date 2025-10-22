import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.004, -0.003).threePointArc((-0.00033, -0.00499), (0.00357, -0.0035)).lineTo(0.00357, 0.0035).threePointArc((-0.00033, 0.00499), (-0.004, 0.003)).lineTo(-0.004, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.007413374876839336)
