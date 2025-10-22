import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00495, 0.03937).lineTo(0.0127, 0.03937).lineTo(0.0127, 0.01041).lineTo(-0.00495, 0.01041).lineTo(-0.00495, 0.03937).close()
solid=wp_sketch0.add(loop0).extrude(0.08178043348063575)
