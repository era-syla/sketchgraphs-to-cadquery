import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0625, 0.0635).lineTo(-0.0175, 0.0635).lineTo(-0.0175, 0.0645).lineTo(-0.0625, 0.0645).lineTo(-0.0625, 0.0635).close()
solid=wp_sketch0.add(loop0).extrude(0.03757330645186155)
