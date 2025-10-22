import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.7907, 2.2987).lineTo(1.7907, 2.2987).lineTo(1.7907, 2.4384).lineTo(-1.7907, 2.4384).lineTo(-1.7907, 2.2987).close()
solid=wp_sketch0.add(loop0).extrude(0.39724553067263474)
