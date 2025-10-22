import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.18613, 0.1565).lineTo(0.1985, 0.1565).lineTo(0.1985, -0.17008).lineTo(-0.18613, -0.17008).lineTo(-0.18613, 0.1565).close()
solid=wp_sketch0.add(loop0).extrude(0.6984730658395123)
