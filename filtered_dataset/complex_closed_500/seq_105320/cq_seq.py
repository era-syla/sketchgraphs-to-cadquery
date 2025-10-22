import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0085, -0.0785).lineTo(0.1385, -0.0785).lineTo(0.1385, 0.0085).lineTo(-0.0085, 0.0085).lineTo(-0.0085, -0.0785).close()
solid=wp_sketch0.add(loop0).extrude(-0.32118606898381274)
