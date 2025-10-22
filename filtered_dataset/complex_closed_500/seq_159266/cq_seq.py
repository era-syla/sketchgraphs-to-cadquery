import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05884, -0.09265).lineTo(-0.04384, -0.09265).lineTo(-0.04384, -0.08965).lineTo(-0.05884, -0.08965).lineTo(-0.05884, -0.09265).close()
solid=wp_sketch0.add(loop0).extrude(-0.04107517878052797)
