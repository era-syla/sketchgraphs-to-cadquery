import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00635, 0.28416).lineTo(0.52626, 0.28416).lineTo(0.52626, -0.28416).lineTo(0.00635, -0.28416).lineTo(0.00635, 0.28416).close()
solid=wp_sketch0.add(loop0).extrude(-1.0318793479921047)
