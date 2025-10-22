import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01317, 0.0).lineTo(0.01778, 0.0).lineTo(0.01778, 0.00292).lineTo(0.01689, 0.00292).lineTo(0.01626, 0.00229).lineTo(0.01626, 0.00082).lineTo(0.01356, 0.00082).lineTo(0.01317, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.009767045393249121)
