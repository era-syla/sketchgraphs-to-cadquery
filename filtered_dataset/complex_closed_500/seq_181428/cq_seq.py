import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0355, 0.11502).lineTo(0.0355, 0.11502).lineTo(0.0355, -0.02458).lineTo(-0.0355, -0.02458).lineTo(-0.0355, 0.11502).close()
solid=wp_sketch0.add(loop0).extrude(-0.3758584079212532)
