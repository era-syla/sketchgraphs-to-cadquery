import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.08991, -0.00637).lineTo(-0.09508, -0.00592).lineTo(-0.09517, -0.00692).lineTo(-0.08999, -0.00737).lineTo(-0.08991, -0.00637).close()
solid=wp_sketch0.add(loop0).extrude(0.0022243556945866507)
