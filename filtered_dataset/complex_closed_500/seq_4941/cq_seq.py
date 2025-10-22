import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.006, 0.188).lineTo(0.506, 0.188).lineTo(0.506, 0.168).lineTo(0.006, 0.168).lineTo(0.006, 0.188).close()
solid=wp_sketch0.add(loop0).extrude(-0.4203285620626047)
