import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.89443, 0.8).lineTo(-1.14281, 0.36605).lineTo(-0.79565, 0.16735).lineTo(-0.54727, 0.6013).lineTo(-0.89443, 0.8).close()
solid=wp_sketch0.add(loop0).extrude(-1.3007362981865174)
