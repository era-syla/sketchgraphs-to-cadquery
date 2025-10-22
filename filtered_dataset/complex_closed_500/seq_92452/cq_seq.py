import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0055, 0.0).lineTo(-0.0055, 0.03253).lineTo(-0.00665, 0.035).lineTo(-0.00665, 0.047).lineTo(-0.0075, 0.04801).lineTo(-0.0075, 0.05).lineTo(-0.0105, 0.05).lineTo(-0.0105, 0.02).lineTo(-0.0075, -0.0).lineTo(-0.0055, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07750051515790583)
