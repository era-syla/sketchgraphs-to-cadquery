import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04445, -0.01905).lineTo(-0.04445, -0.01905).lineTo(-0.04445, 0.01905).lineTo(0.04445, 0.01905).lineTo(0.04445, -0.01905).close()
solid=wp_sketch0.add(loop0).extrude(0.1864598276447607)
