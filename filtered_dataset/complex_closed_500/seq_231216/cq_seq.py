import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00102, 0.02007).lineTo(0.02007, 0.02007).lineTo(0.02007, 0.02769).lineTo(0.00102, 0.02769).lineTo(0.00102, 0.02007).close()
solid=wp_sketch0.add(loop0).extrude(0.0029739420526341755)
