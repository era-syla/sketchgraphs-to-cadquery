import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.111, 0.111).lineTo(0.0, 0.111).lineTo(-0.0, 0.113).lineTo(0.111, 0.113).lineTo(0.111, 0.111).close()
solid=wp_sketch0.add(loop0).extrude(-0.22324652227254224)
