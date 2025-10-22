import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.11307, -0.13).lineTo(-0.11307, -0.13).lineTo(-0.11307, 0.13).lineTo(0.11307, 0.13).lineTo(0.11307, -0.13).close()
solid=wp_sketch0.add(loop0).extrude(0.49114002285239794)
