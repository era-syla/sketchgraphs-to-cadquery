import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03322, 0.045).lineTo(-0.01154, 0.045).lineTo(-0.01154, 0.02595).lineTo(-0.03322, 0.02595).lineTo(-0.03322, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.03547161399479565)
