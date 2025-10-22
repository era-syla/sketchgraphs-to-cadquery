import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.069, 0.08).lineTo(-0.0, 0.08).lineTo(0.0, 0.0).lineTo(0.069, 0.0).lineTo(0.069, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(0.22825923453804847)
