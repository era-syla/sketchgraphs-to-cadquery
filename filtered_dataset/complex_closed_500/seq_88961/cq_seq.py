import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0117, -0.22517).lineTo(0.02256, -0.22517).lineTo(0.02256, -0.19964).lineTo(-0.0117, -0.19964).lineTo(-0.0117, -0.22517).close()
solid=wp_sketch0.add(loop0).extrude(-0.04116855168284286)
