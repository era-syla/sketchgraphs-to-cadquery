import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-3.0, 0.85).lineTo(-5.35, 0.85).lineTo(-5.35, 0.6375).lineTo(-5.6, 0.6375).lineTo(-5.6, 0.425).lineTo(-5.85, 0.425).lineTo(-5.85, 0.2125).lineTo(-6.1, 0.2125).lineTo(-6.1, 0.0).lineTo(-3.0, 0.0).lineTo(-3.0, 0.85).close()
solid=wp_sketch0.add(loop0).extrude(-6.962989331346852)
