import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0175, 0.01425).lineTo(0.0151, 0.01425).lineTo(0.0151, -0.00025).lineTo(-0.0175, -0.00025).lineTo(-0.0175, 0.0).lineTo(-0.0175, 0.01425).close()
solid=wp_sketch0.add(loop0).extrude(0.0012582558693357028)
