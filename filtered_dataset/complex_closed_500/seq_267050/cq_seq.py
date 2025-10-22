import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.11244, 0.12373).lineTo(0.11244, 0.10776).lineTo(0.127, 0.10776).lineTo(0.127, 0.12373).lineTo(0.11244, 0.12373).close()
solid=wp_sketch0.add(loop0).extrude(0.039159730986563605)
