import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0316, 0.11197).lineTo(-0.05352, 0.11197).lineTo(-0.05352, 0.03663).lineTo(0.0316, 0.03663).lineTo(0.0316, 0.11197).close()
solid=wp_sketch0.add(loop0).extrude(0.12768746874329992)
