import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.035, 0.0125).lineTo(-0.035, 0.0125).lineTo(-0.035, -0.0125).lineTo(0.035, -0.0125).lineTo(0.035, 0.0125).close()
solid=wp_sketch0.add(loop0).extrude(-0.06304033570936518)
