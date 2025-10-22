import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03175, 0.0).lineTo(0.0, 0.0).lineTo(0.0, -0.0127).lineTo(-0.0381, -0.0127).lineTo(-0.0381, 0.0127).lineTo(-0.03175, 0.0127).lineTo(-0.03175, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.00465462417951069)
