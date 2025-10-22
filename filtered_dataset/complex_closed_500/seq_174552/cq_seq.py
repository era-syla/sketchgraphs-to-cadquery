import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.23815, -0.02784).lineTo(-0.19315, -0.02784).lineTo(-0.19315, 0.03216).lineTo(-0.23815, 0.03216).lineTo(-0.23815, -0.02784).close()
solid=wp_sketch0.add(loop0).extrude(0.1765733798525274)
