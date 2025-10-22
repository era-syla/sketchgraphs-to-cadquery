import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0135, 0.02791).lineTo(0.0135, 0.0385).lineTo(0.0035, 0.0385).lineTo(0.0035, 0.04).lineTo(0.025, 0.04).lineTo(0.025, 0.0385).lineTo(0.015, 0.0385).lineTo(0.015, 0.02791).lineTo(0.0135, 0.02791).close()
solid=wp_sketch0.add(loop0).extrude(-0.060811485247290326)
