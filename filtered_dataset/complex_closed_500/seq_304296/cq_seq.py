import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01905, 0.0127).lineTo(0.01612, 0.00762).lineTo(0.03468, 0.00762).lineTo(0.03175, 0.0127).lineTo(0.01905, 0.0127).close()
solid=wp_sketch0.add(loop0).extrude(-0.05427313772207171)
