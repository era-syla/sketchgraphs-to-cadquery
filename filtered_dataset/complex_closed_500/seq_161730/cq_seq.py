import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.15339, 0.07986).lineTo(0.15339, 0.07986).lineTo(0.15339, -0.07986).lineTo(-0.15339, -0.07986).lineTo(-0.15339, 0.07986).close()
solid=wp_sketch0.add(loop0).extrude(-0.04916842294994921)
