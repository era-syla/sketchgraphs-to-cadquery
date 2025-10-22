import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.1016, -0.09725).lineTo(0.1016, -0.09725).lineTo(0.1016, 0.10595).lineTo(-0.1016, 0.10595).lineTo(-0.1016, -0.09725).close()
solid=wp_sketch0.add(loop0).extrude(-0.12083985895059002)
