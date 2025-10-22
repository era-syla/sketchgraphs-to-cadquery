import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06134, 0.0).lineTo(-0.05834, 0.0).lineTo(-0.05834, 0.014).lineTo(-0.06134, 0.014).lineTo(-0.06134, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.02733068979227218)
