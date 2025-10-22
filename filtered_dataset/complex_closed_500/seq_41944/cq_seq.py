import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00215, 0.00073).lineTo(0.00215, 0.025).lineTo(-0.03711, 0.025).lineTo(-0.03711, 0.005).lineTo(-0.02323, 0.005).lineTo(-0.03711, -0.0083).lineTo(-0.03711, -0.03688).lineTo(0.00215, 0.00073).close()
solid=wp_sketch0.add(loop0).extrude(0.056910138577864165)
