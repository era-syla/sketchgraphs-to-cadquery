import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0074, 0.0046).lineTo(0.00615, 0.0046).lineTo(0.00615, 0.0076).lineTo(0.0074, 0.0076).lineTo(0.0074, 0.0046).close()
solid=wp_sketch0.add(loop0).extrude(-0.005712991839257609)
