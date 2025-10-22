import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01, 0.0).lineTo(0.01715, 0.0).lineTo(0.01715, 0.03).lineTo(0.01565, 0.03).lineTo(0.01565, 0.003).lineTo(0.01, 0.003).lineTo(0.01, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.06983369681615413)
