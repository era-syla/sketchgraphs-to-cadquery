import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.14019, 0.08862).lineTo(-0.13058, 0.09201).lineTo(-0.13058, 0.09809).lineTo(-0.12139, 0.09583).lineTo(-0.11984, 0.09894).lineTo(-0.11, 0.09216).lineTo(-0.11842, 0.0882).lineTo(-0.10471, 0.08763).lineTo(-0.09157, 0.08198).lineTo(-0.10556, 0.08184).lineTo(-0.12082, 0.0841).lineTo(-0.13397, 0.0858).lineTo(-0.14624, 0.08293).lineTo(-0.14243, 0.08611).lineTo(-0.14485, 0.08961).lineTo(-0.14019, 0.08862).close()
solid=wp_sketch0.add(loop0).extrude(-0.11593279989292198)
