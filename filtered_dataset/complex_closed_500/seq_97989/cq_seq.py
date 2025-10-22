import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.1, 0.0).lineTo(-0.1, 0.15).lineTo(-0.0, 0.15).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.17220515058473074)
