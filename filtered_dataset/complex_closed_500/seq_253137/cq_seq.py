import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.025, 0.13047).lineTo(-0.12959, 0.13047).lineTo(-0.12959, 0.02595).lineTo(-0.025, 0.02595).lineTo(-0.025, 0.13047).close()
solid=wp_sketch0.add(loop0).extrude(0.06288951472912137)
