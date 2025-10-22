import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0).lineTo(0.05532, 0.03885).lineTo(-0.03772, -0.03616).lineTo(-0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.053714906036279965)
