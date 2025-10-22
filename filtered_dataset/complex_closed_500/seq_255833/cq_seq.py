import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03, 0.17).lineTo(0.0, 0.17).lineTo(0.0, 0.14).lineTo(-0.03, 0.14).lineTo(-0.03, 0.17).close()
solid=wp_sketch0.add(loop0).extrude(0.08108934645677769)
