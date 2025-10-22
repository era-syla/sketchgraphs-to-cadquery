import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01829, -0.00547).lineTo(-0.01829, -0.00547).lineTo(-0.01829, 0.00547).lineTo(0.01829, 0.00547).lineTo(0.01829, -0.00547).close()
solid=wp_sketch0.add(loop0).extrude(0.07889565836032082)
